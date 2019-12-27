## Big Data Management (WQD7007) Group Assignment

#### Group Members:
- Cheah Jun Yitt (WQD180107)
- Choo Jian Wei (WQD180124)
- Tan Yin Yen (WQD180108)

## An Efficient Database Management System for Cyber Insurance using Neo4j
This GitHub repository demonstrate the storage and query of a sample dataset on Neo4j. The Microsoft Malware Prediction dataset is chosen and downloaded from [Kaggle](https://www.kaggle.com/c/microsoft-malware-prediction/data). 
Each row in the dataset corresponds to a machine, along with many corresponding attributes and a ground truth label which indicates whether Malware was detected on the machine.
As an example, a few attributes were selected, such as "MachineIdentifier", "Processor", "Census_ProcessorManufacturerIdentifier", "Census_ProcessorModelIdentifier", "Census_MDC2FormFactor", "HasDetections", "Firewall", "OSIdentifier", "CountryIdentifier" and "OrganizationIdentifier", to show the relationships between machines and different attributes.
    
Different tables with selected attributes were created and exported to CSV files to ease the creation of graph in Neo4j. The source code can be found [here](https://github.com/junyitt/bdm-framework/blob/master/Neo4j_ExportCSV.ipynb). 
  
Then, the CSVs were used to create a graph in Neo4j using [these commands](https://github.com/junyitt/bdm-framework/blob/master/Neo4j_commands.txt). Sample queries can be found at the end of text file. The figure below shows the output of the final query command, which is useful to have a visual understanding of what machine type is likely to be affected by Malware.
  
![alt text][graphimg]
[graphimg]: https://raw.githubusercontent.com/junyitt/bdm-framework/master/graph_example.PNG "Query example"
