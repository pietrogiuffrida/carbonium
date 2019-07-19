#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from carbonium import *

if __name__ == '__main__':

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

    structure = Structure(name_list)

    print(structure.names)
    print(structure.domains)

    print(
        structure.var1.name,
        structure.var1.domains,
        structure.var1.output_order
    )

    print(structure.get_names('raw'))

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