from ai_common.file_operations import get_project_path
from classify_images import classify_images

# Path to pet_images relative to project root
img_dir = get_project_path("src/intropyproject_classify_pet_images/data/pet_images")


def test_vgg(labels):
    model = "vgg"
    classify_images(img_dir, labels, model)
    assert labels["Poodle_07927.jpg"] == ["poodle", "standard poodle, poodle", 1]
    print(dict(labels))


def test_resnet(labels):
    model = "resnet"
    classify_images(img_dir, labels, model)
    assert labels["Poodle_07927.jpg"] == ["poodle", "standard poodle, poodle", 1]
    # print(dict(labels))


def test_alexnet(labels):
    model = "alexnet"
    classify_images(img_dir, labels, model)
    assert labels["Poodle_07927.jpg"] == ["poodle", "standard poodle, poodle", 1]
    # print(dict(labels))
