# Running Debris Flow Model on Tufts Cluster

1. Login to Cluster.
2. Go to patralab group space dir.

## Running a Single Simulation

- Make dir for the simulation

    ```bash
    mkdir test_simulation
    cd test_simulation
    ```

- Copy all the files from `<PATH_TO_titan2d_scripts>/temp_sim` to current dir

    ```bash
    cp -r <PATH_TO_titan2d_scripts>/temp_sim/* ./
    ```

- Copy `<PATH_TO_titan2d_scripts>/run_titan_debrisflow.sh` to current dir

    ```bash
    cp <PATH_TO_titan2d_scripts>/run_titan_debrisflow.sh ./
    ```

- Check `<PATH_to_titan2d>` and `<PATH_to_model_parameters.py>` in `run_titan_debrisflow.sh`

- Update Simulation Parameters

- Update `input.py`