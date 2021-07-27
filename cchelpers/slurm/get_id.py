import os
import glob


def get_id(base_dir: str, job_hash: str) -> int:
    job_folder = os.path.join(base_dir, job_hash)

    slurm_files = glob.glob(os.path.join(job_folder, "slurm-*.out"))
    if len(slurm_files) == 0:
        return None
    elif len(slurm_files) != 1:
        raise FileExistsError(
            "Found {} slurm files for job {}, expected one only.".format(
                len(slurm_files), job_hash))
    else:
        slurm_file = slurm_files[0]
        slurm_id = int(
            os.path.split(slurm_file)[1].replace("slurm-",
                                                 "").replace(".out", ""))
        return slurm_id
