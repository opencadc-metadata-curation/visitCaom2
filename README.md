# visitcaom2
An application to visit CAOM2 Observations without access to FITS files.

# How to Run visit

In an empty directory (the 'working directory'), on a machine with Docker installed:

1. In the master branch of this repository, find the scripts directory, and copy the file visit_run.sh to the working directory. e.g.:

  ```
  wget https://raw.github.com/opencadc-metadata-curation/visitCaom2/master/scripts/visit_run.sh
  ```

2. Create a text file named `todo.txt`. This file will have all the observationIDs that require repair, one ID per line. e.g.:

  ```
  20090629-a96458f347efa3cbcd0f28171743e9cb
  20150612-418df74888cfeff1651599d5703218a1
  acsis_00015_20070529T090717
  ...
  ```
3. Ensure the script is executable:

```
chmod +x visit_run.sh
```

4. To run the application:

```
./visit_run.sh
```

The `config.yml` file will be created the first time `visit_run.sh` is executed. It may then be modified.
