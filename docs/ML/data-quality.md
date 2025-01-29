---
layout: default
title: Data Quality Assurance and Governance
parent: Machine Learning
---

# Data Quality Assurance and Governance

All our decisions in today's world of Big Data are data-driven—even when we are heading to college or any other place. Navigation apps help us find the best route to reach a particular destination. They achieve this based on data that has been fed into them. Recognizing the fact that our decisions are data-driven, it is crucial to ensure that we have high-quality data. The research paper *"Everyone Wants to Do the Model Work, Not the Data Work"* indicated that data quality often plays down the challenge in AI systems. [[1]](https://dl.acm.org/doi/abs/10.1145/3411764.3445518)

![alt text](../../../assets/images/ml/data/1.jpeg)

## The Problem of Data Quality

In the real world, perfect data quality everywhere is not possible. Yet still, humans manage to move forward despite these problems. Achieving data quality is also an essential task in any data-driven area.

In this blog, I will go through how to ensure the quality of data. My main concentration will be on primary data and, to some extent, secondary data.

### Understanding Primary and Secondary Data

#### Primary Data
Data collected through immediate methods of research or model builders by direct surveys, experiments, etc., is known as primary data. It is fresh and original data collected with a specific objective in mind.

#### Secondary Data
Secondary data is information gathered by others for other purposes. These come from government reports, research papers, old historical databases, or published industry periodicals.

![alt text](../../../assets/images/ml/data/2.jpeg)

[_Diagram from mermaid mind_](https://mermaid-mind.vercel.app/gallery/6799d5e08192d3f5b911fd01)

## Quality Assurance of Primary Data

Depending on the quality of the collection, primary data have different qualities. Some ways that one could achieve good data quality are as follows:

Here's a detailed description of techniques for ensuring primary data quality:

- **Defining Standard Variables**

Uniform variable names and formats across all data collection instruments ensure that people are not confused and that everything makes sense. For example, using 'customer_id' instead of 'cust_id' or 'customerID' for the same concept allows more dependability when integrating data or making analyses.

- **Units of Measurement**

Specifying and enforcing consistent units of measurement throughout the data collection process avoids conversion errors and misinterpretation. This involves clearly documenting whether measurements are in metric or imperial units, and maintaining the same unit system for all related data points.

- **Data Type Constraints**

Implementing strict data type validation ensures that each field contains appropriate information in the correct format. This involves setting up proper data types (integer, string, date, etc.) and field length restrictions to maintain data integrity and prevent invalid entries.

- **Predefined Validation Messages**

Creating clear, informative error messages that appear when data entry rules are violated helps users understand and correct mistakes immediately. These messages should guide users on proper data format and acceptable values, reducing the likelihood of incorrect data submission.

- **Dropdown Menus**

The use of dropdown lists for fields with pre-defined options eliminates spelling errors and ensures consistency in data entry. This approach also accelerates data entry and reduces the cognitive load on users by providing them with valid choices rather than requiring manual input.

- **Acknowledgments**

Confirmation steps or acknowledgments also mean that users must verify critical data entered before submission. This entails an extra layer of quality control and increased accountability on the part of the user regarding the accuracy of their entries.

- **Metadata Language**

Developing detailed metadata documentation that describes data elements, their interrelationship, and context ensures long-term usability and understanding of data. This includes definite definitions, data dictionaries, and documentation of changes in updates to the data structure.

- **Question Relevance**

Ensuring that data collection questions are relevant to the research objectives and are clear to the respondents enhances response quality. This requires careful design and testing of questions to ensure that each item captures the information intended.

![alt text](../../../assets/images/ml/data/3.jpg)

## Quality Control of Secondary Data

Secondary data is collected from sources outside of the researcher's control. The following steps must be taken to ensure the quality of secondary data:

1. **Source Credibility**
   - Determine the credibility of the data source.
   - Compare different sources for accuracy.

2. **Relevance and Timeliness**
   - Verify the date of publication to be sure that the data is current.
   - Determine whether the data works for the present research or business requirement.

3. **Data Consistency**
   - Identify differences in similar datasets.
   - Detect anomalies by the use of statistical methods.

4. **Data Transformation and Standardization**
   - Convert data into one structure.
   - Normalize techniques for consistency of datasets.

## Conclusion

All data-driven decision-making processes rely on the quality assurance and governance of data. Working with primary or secondary data requires best practices when collecting, validating, and pre-processing to ensure reliable outputs and performance of the model.

When there are strict data quality measures implemented, organizations can improve the overall reliability of their data, thereby leading to more effective, accurate, and impactful decision-making.

## References

1. [Everyone Wants to Do the Model Work, Not the Data Work](https://dl.acm.org/doi/abs/10.1145/3411764.3445518)
2. [Top 10 Data Quality Best Practices to Improve Data Performance - Atlan](https://atlan.com/data-quality-best-practices/)
