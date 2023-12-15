import fiftyone as fo
import fiftyone.zoo as foz

# Specify dataset type ("train", "validation")
dataset_type = "train"  # or "train"

# Specify classes to download
classes = ["cat", "dog"]

# Specify number of samples to download 
max_samples = 1000 

# Load the dataset
dataset = foz.load_zoo_dataset(
    "coco-2017",
    split=dataset_type,
    classes=classes,
    max_samples=max_samples,
    dataset_dir="./coco-2017"  # specify download path
)

# Explore the dataset in the FiftyOne App
session = fo.launch_app(dataset)
