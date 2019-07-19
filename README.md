# carbonium

Easily manage a list of names with several
property and (overlapping) order criteria.

## Installation

Install carbonium is as easy as run 
```pip install carbonium```.

## Usage

As first step you should define a name list:

```python
name_list = [
    {
        "domains": ["raw", "output"],
        "name": "var1",
        "alias": "column_1_name",
        "output_order": 1,
        "filling_value": 10,
    },
    {
        "domains": ["raw"],
        "name": "var2",
        "alias": "column_2_name",
        "output_order": 2,
    },
    {
        "domains": ["new", "output"],
        "name": "new_var",
        "alias": "new_column_name",
    },
]
```

Each *name definition* is a dictionary that
contains some common, mandatory key, and some
other keys, domain-specific or name-specific.

Mandatory keys are only three:

- domains, a list of string, each representing a *domain*
- name, a string, uniquely identifiers of a *name*
- alias, a string that can be used to refers to
    the name in context where it is named with
    this alternative string.
    
Then, each name belongs to some domains. Domains
are used to perfom names selection (give me all
names belonging to *domain*). Names that belongs
to the same domain should have the same optional
attributes.

After *name list* definition, you can instantiate
the structure class:

```python
from carbonium import Structure

structure = Structure(name_list)
```

Internally, the Structure class iteratively instantiate a
Name class for each *name definition*. After this
step you can access to each Name and its properties
through ```c``` object, but you can also use one of
property or method of the class.

```python
print(structure.names)
# returns:  ['var1', 'var2', 'new_var']

print(structure.domains)
# returns: {'new', 'output', 'raw'}

print(
    structure.var1.name,
    structure.var1.domains,
    structure.var1.output_order
)
```

Calling *structure.var1.name* you have access to the
string associated to var1... and so on.

```python
ordered_raw_columns = [
        (
            i,
            structure.get(i).output_order,
            structure.get(i).get("filling_value")
        )
        for i in structure.get_names('raw')
]

ordered_raw_columns = sorted(
    ordered_raw_columns,
    key=lambda x: x[1]
)
```

In this example all the names belonging to *raw*
domain are extracted with some other properties.
In this way the same name can be used in different
domains or contexts by referring to contexctual
relevant properties.

```python
import pandas as pd
df = pd.DataFrame([
    {"var1": 100, "var2": 200},
    {"var2": 220},
])

for name in structure.get_names('raw'):
    filling = structure.get(name).get("filling_value")
    if filling:
        df[name].fillna(filling, inplace=True)

for name in structure.get_names('new'):
    df[name] = "arbitrary"    

output_columns = structure.get_names('new')
df[output_columns].to_parquet('output.parquet')
```

As you can see, whithout modify the code but only the
taxonomy described in *name_list*, you can affect
different columns.