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

- Updated `run_titan_debrisflow.sh`
  - Check `<PATH_to_titan2d>` and `<PATH_to_model_parameters.py>` in `run_titan_debrisflow.sh`
  - Update Simulation Parameters

- Update `input.py`
  - Check for DEMs info in `sim.setGIS()`
  - Add Dummy Pile in the simulation region using `sim.addPile()`
  - Check for `max_time` and `max_iter` in `setTimeProps()`

- Log-in to Computational Node

- Execute `run_titan_debrisflow.sh`

    ```bash
    source run_titan_debrisflow.sh
    ```

## Running a set of Ensemble

- Make dir for the Ensemble where you want all the runs to stored

    ```bash
    mkdir test_ensemble
    cd test_ensemble
    ```

- Copy `temp_sim` from `<PATH_TO_titan2d_scripts>` to your current dir

    ```bash
    cp -r <PATH_TO_titan2d_scripts>/temp_sim ./
    ```

- (Optional) Copy following files from `<PATH_TO_titan2d_scripts>` to your current dir

    ```bash
    cp <PATH_TO_titan2d_scripts>/model_parameters.py ./
    cp <PATH_TO_titan2d_scripts>/example_data/Latin_model_parameters_mask.txt ./
    ```

- Copy `<PATH_TO_titan2d_scripts>/run_ensemble.sh` to current dir

    ```bash
    cp <PATH_TO_titan2d_scripts>/run_ensemble.sh ./
    ```

- Update `run_ensemble.sh`:
  - Check path for `parameter_design_file`
  - Update `n_start` and `n_stop`
  - Check path for `temp_sim` (Simulation Template DIR)
  - Check path for `model_parameters.py`
  - Check path for `slurm_file`

- Update `temp_sim/input.py`:
  - Check for DEMs info in `sim.setGIS()`
  - Add Dummy Pile in the simulation region using `sim.addPile()`
  - Check for `max_time` and `max_iter` in `setTimeProps()`

- Execute `run_ensemble.sh`

    ```bash
    source run_ensemble.sh
    ```
