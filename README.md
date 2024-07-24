# Nutri-Score 2023

## Table of Contents

1. [Introduction](#introduction)
2. [Calculation method](#calculation-method)
3. [Score interpretation](#score-interpretation)
4. [Nutrition profile](#nutrition-profile)

# Introduction

The Nutri-Score, standardized and endorsed by the European Union, is a nutrition label that helps consumers understand the nutritional quality of food products at a glance. It was developed to address the increasing need for clear, accessible nutrition information in order to make healthier food choices.

The nutri score in this package is calculated based on the updated 2023 algorithm specified in the document on the following link:
https://www.santepubliquefrance.fr/en/nutri-score.

# Calculation method

Brief summary of factors that affect of nutri-score is as follows:

1. Food type

There are three main food categories, with each type having a different scoring criteria:

-   General food (with subcategories: red meat and cheese)
-   Fats, oils, nuts and seeds
-   Beverages

2. Nutrient content

Points are calculated based on the amount of the following nutrients per 100g of food:

Negative points:

-   Energy
-   Saturated fat
-   Sugars
-   Sodium

Positive points:

-   Protein
-   Fiber
-   Fruits, vegetables, legumes pecentage

The final score is the subtraction of positive points from negative points.

# Score interpretation

The score is converted to a category (A to E) based on the following thresholds, with A being the healthiest and E being the least healthy:

| General Foods | Fats, Nuts and Seeds | Beverages | Category |
| ------------- | -------------------- | --------- | -------- |
| min to 0      | min to -6            | waters    | A        |
| 1 to 2        | -5 to 2              | min to 2  | B        |
| 3 to 10       | 3 to 10              | 3 to 6    | C        |
| 11 to 18      | 11 to 18             | 7 to 9    | D        |
| 19 to max     | 19 to max            | 10 to max | E        |

# Nutrition profile

This package also allows users to set a nutrition profile. Basically, the nutrition profile refers to how strict the user wants to be with the consumption of certain nutrients.
Currently, there are component profiles for:

-   Energy (or energy from saturated fat for fats, and oils, nuts and seeds)
-   Saturated fat (or ratio of saturated fat to total fat for fats, and oils, nuts and seeds)
-   Sugars
-   Sodium

By default, all profile factors are set to 1. If a profile factor is greater than 1, it means that the user wants to be more strict with that component. If the factor is smaller than 1, it means that the user wants to be more flexible with that component.

For example, if sugars profile is set to 1.5, it means that consuming 10 grams of sugars will incur the same amount of negative points as consuming 15 grams of sugars under default setting.
