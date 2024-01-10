import ray

# Initialize Ray
if ray.is_initialized():
    ray.shutdown()
ray.init()

print(ray.cluster_resources())
num_workers = 6  # prefer to do a few less than total available CPU (1 for head node + 1 for background tasks)
resources_per_worker={"CPU": 1, "GPU": 0}