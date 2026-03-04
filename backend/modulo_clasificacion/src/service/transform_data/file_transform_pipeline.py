import pandas as pd

from ...infrastructure.file_reader.read_file_manager import FileReader


class TransformDataFrame:

    def __init__(self, df:pd.DataFrame, tipo_base:str, tipo_base_inicial:str):
        self.df = df
        self.tipo_base = tipo_base
        self.tipo_base_inicial = tipo_base_inicial

        self.YAML_FILE_PATH_TRANSFORM_RULES = r'modulo_clasificacion\src\service\transform_data\pandas_transform_files_rules.yaml'
        self.YAML_FILE_PATH_COLUMNS_RESTRICTION = r'modulo_clasificacion\src\service\transform_data\columns_mapping_base_inicial.yaml'

    def pipeline_transform_data(self):

        df_add_columns = self.subprocess_add_columns(self.df)

        df_select_columns = self.subprocess_select_columns(df_add_columns)

        df_rename_columns = self.subprocess_rename_columns(df_select_columns)

        df_drop_duplicates = self.subprocess_drop_duplicates(df_rename_columns)

        df_drop_na = self.subprocess_drop_na_values(df_drop_duplicates)
        
        df_change_type_str = self.subprocess_change_type_to_str(df_drop_na)

        return df_change_type_str


    def subprocess_recreate_dataframe(self):
        """
        Docstring for subprocess_rename_cols
        
        
        """

        parameters = FileReader().open_yaml_content(file_path=self.YAML_FILE_PATH_COLUMNS_RESTRICTION)

        columns_from_original_base = parameters["renamed_columns_name"][self.tipo_base_inicial]

        expected_columns_df = self.df.rename(columns=columns_from_original_base)

        required_columns = parameters["required_columns"]["final"]

        not_in_list = set ( required_columns ) - set ( expected_columns_df.columns)

        expected_columns_df[list ( not_in_list ) ] = None

        expected_columns_df = expected_columns_df[required_columns]

        return expected_columns_df
        

    def subprocess_add_columns(self, df):

        parameters = FileReader().open_yaml_content(file_path=self.YAML_FILE_PATH_TRANSFORM_RULES)
        
        add_columns_df = parameters["base"][self.tipo_base]["add_columns"]

        df[add_columns_df] = None

        return df


    def subprocess_select_columns(self, df:pd.DataFrame):

        parameters = FileReader().open_yaml_content(file_path=self.YAML_FILE_PATH_TRANSFORM_RULES)
        required_columns_list = parameters["base"][self.tipo_base]["required_columns"]

        df = df[required_columns_list]

        return df

    def subprocess_rename_columns(self, df:pd.DataFrame):
        
        parameters = FileReader().open_yaml_content(file_path=self.YAML_FILE_PATH_TRANSFORM_RULES)
        renamed_columns_list = parameters["base"][self.tipo_base]["expected_columns_name"]

        df.columns = renamed_columns_list 

        return df

    def subprocess_drop_duplicates(self, df:pd.DataFrame):

        parameters = FileReader().open_yaml_content(file_path=self.YAML_FILE_PATH_TRANSFORM_RULES)

        
        if "drop_duplicates" in parameters["base"][self.tipo_base].keys():

            drop_by_value = parameters["base"][self.tipo_base]["drop_duplicates"]
            df = df.drop_duplicates(subset=drop_by_value)

        return df
    
    def subprocess_drop_na_values(self, df:pd.DataFrame):

        parameters = FileReader().open_yaml_content(file_path=self.YAML_FILE_PATH_TRANSFORM_RULES)


        if "drop_na" in parameters["base"][self.tipo_base].keys():
            
            drop_by_na = parameters["base"][self.tipo_base]["drop_na"]
            df = df.dropna(subset=drop_by_na)
        
        return df
    
    def subprocess_change_type_to_str(self, df:pd.DataFrame):

        parameters = FileReader().open_yaml_content(file_path=self.YAML_FILE_PATH_TRANSFORM_RULES)

        if "change_type_to_str" in parameters["base"][self.tipo_base].keys():
            
            field_to_change = parameters["base"][self.tipo_base]["change_type_to_str"]
            
            for col in field_to_change:
                df[col] = df[col].astype('str').str.strip()
        
        return df