from get_pet_labels import get_pet_labels


def test_get_directory(labels):
    img_dir = "src/intropyproject_classify_pet_images/data/pet_images"
    result = get_pet_labels(img_dir)
    assert result == labels
