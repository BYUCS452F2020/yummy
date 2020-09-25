# Yummy: SQL Schema

## Recipe Table
Description: It is the collection of all recipes

Represents: Each instance represents a recipe

Normalization: This table is normalized because all columns are atomic  and the non-key columns only depend on the candidate keys

>   Recipe (<ins>RecipeID</ins>, AuthorID, Name, Duration, Description, Picture, Difficulty, Style, Country, Course)
> * Foreign Key AuthorID references User


| Column        | Description   |
| ------------- |:-------------:|
| RecipeID      | Integer       |
| AuthorID      | Integer       |
| Name          | String        |
| Duration      | String { 1hr, 30min, …}   |
| Picture       | Blob          |
| Difficulty    | Integer { 1 - 5 }         |
| Style         | String { Roasted, Fried, Steamed, ... }       |
| Country       | String { French, Korean, American, … }        |
| Course        | String { appetizer, main, dessert, snack }    |


## Ingredient Table
Description: It is the set of all ingredients for each recipe

Normalization: This table is normalized because all columns are atomic and the non-key columns only depend on the candidate keys

>   Ingredient (<ins>RecipeID</ins>, <ins>Name</ins>, Amount) - composite key
> *	Foreign Key RecipeID references RecipeID

| Column        | Description   |
| ------------- |:-------------:|
| RecipeID      | Integer       |
| Name          | String        |
| Amount        | String { 5 cups, ... }        |


## Procedure Table
Description: It is the set of all procedure for each recipe

Normalization: This table is normalized because all columns are atomic and the non-key columns only depend on the candidate keys

>   Procedure Table (<ins>RecipeID</ins>, <ins>Procedure</ins>, Description) - composite key
> *	Foreign Key RecipeID reference RecipeID

| Column        | Description   |
| ------------- |:-------------:|
| RecipeID      | Integer       |
| Procedure     | Integer { 1, 2, 3, ... }       |
| Description   | String        |


## User Table
Description: It is the collection of all users

Normalization: This table is normalized because all columns are atomic and the non-key columns only depend on the candidate keys

>   User (<ins>UserID</ins>, Username, Password, Email) 

| Column        | Description   |
| ------------- |:-------------:|
| UserID        | Integer       |
| Username      | String        |
| Password      | String #unecrypted        |
| Email         | String        |


## Flavorite Table
Description: It is the collection of all favorite recipes for each user

Normalization: This table is normalized because all columns are atomic and the non-key columns only depend on the candidate keys

>   Flavorite (<ins>UserID</ins>, <ins>RecipeID</ins>) - Composite Key
> *	Foreign Key references UserID
> *	Foreign Key references RecipeID

| Column        | Description   |
| ------------- |:-------------:|
| UserID        | Integer       |
| RecipeID      | Integer       |