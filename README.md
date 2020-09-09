# visitcaom2
An application to visit CAOM2 Observations without access to FITS files.

# How to Run visit

In an empty directory (the 'working directory'), on a machine with Docker installed:

1. In the master branch of this repository, find the scripts directory, and copy the file visit_run.sh to the working directory. e.g.:

  ```
  wget https://raw.github.com/opencadc-metadata-curation/visitCaom2/master/scripts/visit_run.sh
  ```

2. Ensure the script is executable:

```
chmod +x visit_run.sh
```

3. To run the application:

```
./visit_run.sh
```

The `config.yml` file will be created the first time `visit_run.sh` is executed. It may then be modified.
