import pytest
import nutri_score as ns
from nutri_score import NutriScoreCalculator

# energy, saturated_fat, sugars, sodium, protein, fiber, fruit_percentage, food_type, expected_score, expected_category
TEST_DATA_GENERAL_FOOD = [
    [321, 0, 17.1, 0, 0.2, 1.9, 90, ns.GENERAL_FODD, 0, "A"],  # Apple sauce
    [0, 0, 0, 84.5, 0, 0, 0, ns.GENERAL_FODD, 20, "E"],  # Sea salt
    [1700, 0, 100, 0, 0, 0, 0, ns.GENERAL_FODD, 20, "E"],  # Granulated Sugar
    [489, 0.9, 0, 0.1, 23.7, 0, 0, ns.RED_MEAT, -1, "A"],  # Beef tenderloin steak raw
    [653, 2.8, 0, 0.1, 23.2, 0, 0, ns.RED_MEAT, 1, "B"],  # Pork laoin chop raw
    [908, 7.1, 0, 0.2, 19.3, 0, 0, ns.RED_MEAT, 7, "C"],  # Minced lamb raw
    [1025, 6.0, 0.5, 0.2, 22.4, 0, 0, ns.RED_MEAT, 6, "C"],  # Pork square rib prepared
    [1523, 19.8, 0.5, 1.8, 24, 0, 0, ns.CHEESE, 15, "D"],  # Cheese
    [1568, 20.2, 0, 1.8, 26, 0, 0, ns.CHEESE, 15, "D"],  # Solid cheese
    [1344, 18.4, 2.6, 1.6, 15, 0, 0, ns.CHEESE, 15, "D"],  # Soft cheese
    [1242, 15.6, 1.0, 2.3, 19, 0, 0, ns.CHEESE, 17, "D"],  # Processed cheese
]

#  energy_from_saturates, saturates_over_total_fat, sugars, sodium, protein, fiber, fruit_percentage, food_type, expected_score, expected_category
TEST_DATA_FATS_NUTS_SEEDS = [
    [2024, 67.3, 0.9, 0.6, 0.7, 0, 0, ns.FATS_NUTS_SEEDS, 22, "E"],  # Animal fat
    [1055, 50.1, 0.8, 0.7, 0.5, 0, 0, ns.FATS_NUTS_SEEDS, 18, "D"],  # Margarine
    [773, 24.4, 0.2, 0.6, 0.2, 0, 0, ns.FATS_NUTS_SEEDS, 11, "D"],  # Baking fat
    [244, 14.5, 7.8, 1.1, 18.7, 6.0, 0, ns.FATS_NUTS_SEEDS, 7, "C"],  # Nuts and seeds
    [237, 12.9, 11.2, 0, 17.2, 7.3, 0, ns.FATS_NUTS_SEEDS, -6, "A"],  # Nuts and seeds (plain)
    [363, 18.6, 6.9, 0.6, 21.9, 7.9, 0, ns.FATS_NUTS_SEEDS, 4, "C"],  # Nut butter
]

# energy, saturated_fat, sugars, sodium, nn_sweeteners, protein, fiber, fruit_percentage, food_type, expected_score, expected_category
TEST_DATA_BEVERAGES = [
    [201, 0, 9.0, 0, False, 0.5, 0, 100, ns.BEVERAGES, 4, "C"],  # Orange juice
    [29, 0, 1.2, 0, True, 0.1, 0, 0, ns.BEVERAGES, 5, "C"],  # Soft drink with sweeteners
    [176, 0, 10.6, 0, False, 0, 0, 0, ns.BEVERAGES, 12, "E"],  # Soft drink
    [0, 0, 0, 0, False, 0, 0, 0, ns.WATER, 0, "A"],  # Water
]


@pytest.mark.parametrize("index", range(len(TEST_DATA_GENERAL_FOOD)))
def test_general_food(index: int):
    (
        energy,
        saturated_fat,
        sugars,
        sodium,
        protein,
        fiber,
        fruit_percentage,
        food_type,
        expected_score,
        expected_category,
    ) = TEST_DATA_GENERAL_FOOD[index]

    calculator = NutriScoreCalculator()
    nutritions = {
        ns.ENERGY: energy,
        ns.SATURATED_FAT: saturated_fat,
        ns.SUGARS: sugars,
        ns.SODIUM: sodium,
        ns.PROTEIN: protein,
        ns.FIBER: fiber,
        ns.FRUIT_PERCENTAGE: fruit_percentage,
    }
    score = calculator.calculate(nutritions, food_type)
    category = calculator.categorize(score, food_type)
    assert score == expected_score
    assert category == expected_category


@pytest.mark.parametrize("index", range(len(TEST_DATA_FATS_NUTS_SEEDS)))
def test_fats_nuts_seeds(index: int):
    (
        energy_from_saturates,
        saturates_over_total_fat,
        sugars,
        sodium,
        protein,
        fiber,
        fruit_percentage,
        food_type,
        expected_score,
        expected_category,
    ) = TEST_DATA_FATS_NUTS_SEEDS[index]

    calculator = NutriScoreCalculator()
    nutritions = {
        ns.ENERGY_FROM_SATURATES: energy_from_saturates,
        ns.SATURATES_OVER_TOTAL_FAT: saturates_over_total_fat,
        ns.SUGARS: sugars,
        ns.SODIUM: sodium,
        ns.PROTEIN: protein,
        ns.FIBER: fiber,
        ns.FRUIT_PERCENTAGE: fruit_percentage,
    }
    score = calculator.calculate(nutritions, food_type)
    category = calculator.categorize(score, food_type)
    assert score == expected_score
    assert category == expected_category


@pytest.mark.parametrize("index", range(len(TEST_DATA_BEVERAGES)))
def test_beverages(index: int):
    (
        energy,
        saturated_fat,
        sugars,
        sodium,
        nn_sweeteners,
        protein,
        fiber,
        fruit_percentage,
        food_type,
        expected_score,
        expected_category,
    ) = TEST_DATA_BEVERAGES[index]

    calculator = NutriScoreCalculator()
    nutritions = {
        ns.ENERGY: energy,
        ns.SATURATED_FAT: saturated_fat,
        ns.SUGARS: sugars,
        ns.SODIUM: sodium,
        ns.NN_SWEETENERS: nn_sweeteners,
        ns.PROTEIN: protein,
        ns.FIBER: fiber,
        ns.FRUIT_PERCENTAGE: fruit_percentage,
    }
    score = calculator.calculate(nutritions, food_type)
    category = calculator.categorize(score, food_type)
    assert score == expected_score
    assert category == expected_category
