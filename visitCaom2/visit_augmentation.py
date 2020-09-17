# -*- coding: utf-8 -*-
# ***********************************************************************
# ******************  CANADIAN ASTRONOMY DATA CENTRE  *******************
# *************  CENTRE CANADIEN DE DONNÉES ASTRONOMIQUES  **************
#
#  (c) 2020.                            (c) 2020.
#  Government of Canada                 Gouvernement du Canada
#  National Research Council            Conseil national de recherches
#  Ottawa, Canada, K1A 0R6              Ottawa, Canada, K1A 0R6
#  All rights reserved                  Tous droits réservés
#
#  NRC disclaims any warranties,        Le CNRC dénie toute garantie
#  expressed, implied, or               énoncée, implicite ou légale,
#  statutory, of any kind with          de quelque nature que ce
#  respect to the software,             soit, concernant le logiciel,
#  including without limitation         y compris sans restriction
#  any warranty of merchantability      toute garantie de valeur
#  or fitness for a particular          marchande ou de pertinence
#  purpose. NRC shall not be            pour un usage particulier.
#  liable in any event for any          Le CNRC ne pourra en aucun cas
#  damages, whether direct or           être tenu responsable de tout
#  indirect, special or general,        dommage, direct ou indirect,
#  consequential or incidental,         particulier ou général,
#  arising from the use of the          accessoire ou fortuit, résultant
#  software.  Neither the name          de l'utilisation du logiciel. Ni
#  of the National Research             le nom du Conseil National de
#  Council of Canada nor the            Recherches du Canada ni les noms
#  names of its contributors may        de ses  participants ne peuvent
#  be used to endorse or promote        être utilisés pour approuver ou
#  products derived from this           promouvoir les produits dérivés
#  software without specific prior      de ce logiciel sans autorisation
#  written permission.                  préalable et particulière
#                                       par écrit.
#
#  This file is part of the             Ce fichier fait partie du projet
#  OpenCADC project.                    OpenCADC.
#
#  OpenCADC is free software:           OpenCADC est un logiciel libre ;
#  you can redistribute it and/or       vous pouvez le redistribuer ou le
#  modify it under the terms of         modifier suivant les termes de
#  the GNU Affero General Public        la “GNU Affero General Public
#  License as published by the          License” telle que publiée
#  Free Software Foundation,            par la Free Software Foundation
#  either version 3 of the              : soit la version 3 de cette
#  License, or (at your option)         licence, soit (à votre gré)
#  any later version.                   toute version ultérieure.
#
#  OpenCADC is distributed in the       OpenCADC est distribué
#  hope that it will be useful,         dans l’espoir qu’il vous
#  but WITHOUT ANY WARRANTY;            sera utile, mais SANS AUCUNE
#  without even the implied             GARANTIE : sans même la garantie
#  warranty of MERCHANTABILITY          implicite de COMMERCIALISABILITÉ
#  or FITNESS FOR A PARTICULAR          ni d’ADÉQUATION À UN OBJECTIF
#  PURPOSE.  See the GNU Affero         PARTICULIER. Consultez la Licence
#  General Public License for           Générale Publique GNU Affero
#  more details.                        pour plus de détails.
#
#  You should have received             Vous devriez avoir reçu une
#  a copy of the GNU Affero             copie de la Licence Générale
#  General Public License along         Publique GNU Affero avec
#  with OpenCADC.  If not, see          OpenCADC ; si ce n’est
#  <http://www.gnu.org/licenses/>.      pas le cas, consultez :
#                                       <http://www.gnu.org/licenses/>.
#
#  : 4 $
#
# ***********************************************************************
#

import logging
from caom2 import Observation
from caom2pipe import manage_composable as mc


def visit(observation, **kwargs):
    mc.check_param(observation, Observation)
    count = 0
    changed = False

    for plane in observation.planes.values():
        for artifact in plane.artifacts.values():
            if '.sdf' in artifact.uri:
                # GB 15=09-20
                # ignore sdf files as they aren't cutout candidates
                continue
            for part in artifact.parts.values():
                for chunk in part.chunks:
                    n_axis_count = 0
                    if chunk.position is None:
                        if (chunk.position_axis_1 is not None or
                                chunk.position_axis_2 is not None):
                            chunk.position_axis_1 = None
                            chunk.position_axis_2 = None
                            changed = True
                    else:
                        if (chunk.position_axis_1 is None or
                                chunk.position_axis_2 is None):
                            chunk.position_axis_1 = 1
                            chunk.position_axis_2 = 2
                            changed = True
                            n_axis_count = 2

                    if chunk.energy is None:
                        if chunk.energy_axis is not None:
                            chunk.energy_axis = None
                            changed = True
                    else:
                        n_axis_count += 1
                        if chunk.energy_axis is None:
                            chunk.energy_axis = n_axis_count
                            changed = True

                    if chunk.observable is None:
                        if chunk.observable_axis is not None:
                            chunk.observable_axis = None
                            changed = True
                    else:
                        n_axis_count += 1
                        if chunk.observable_axis is None:
                            chunk.observable_axis = n_axis_count
                            changed = True

                    if chunk.custom is None:
                        if chunk.custom_axis is not None:
                            chunk.custom_axis = None
                            changed = True

                    if chunk.polarization is None:
                        if chunk.polarization_axis is not None:
                            chunk.polarization_axis = None
                            changed = True
                    else:
                        n_axis_count += 1
                        if chunk.polarization_axis is None:
                            chunk.polarization_axis = n_axis_count
                            changed = True

                    if changed:
                        chunk.naxis = n_axis_count if n_axis_count > 0 else None
                        count += 1
                        changed = False
    logging.info(f'Changing {count} chunks for {observation.observation_id}.')
    return {'chunks': count}
