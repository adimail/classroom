---
layout: default
title: Data Quality Assurance and Governance
parent: Machine Learning
---

# Data Quality Assurance and Governance

In today's world of Big Data, all our decisions are data-driven—even when we are heading to college or any other place. Navigation apps help us find the best route to reach a particular destination. They achieve this based on data that has been fed into them. Recognizing the fact that our decisions are data-driven, it is crucial to ensure that we have high-quality data. The research paper *"Everyone Wants to Do the Model Work, Not the Data Work"* highlights the often-overlooked issue of data quality in AI systems. [[1]](https://dl.acm.org/doi/abs/10.1145/3411764.3445518)

![alt text](../../../assets/images/ml/data/1.jpeg)

## The Challenge of Data Quality

In the real world, achieving perfect data quality everywhere is practically impossible. However, humans still manage to move forward despite these challenges. Ensuring data quality remains a vital task in any data-driven domain.

In this blog, I will cover how we can ensure data quality. My main focus will be on primary data and, to some extent, secondary data.

### Understanding Primary and Secondary Data

#### Primary Data
Primary data is collected directly by researchers or model developers through surveys, experiments, or other techniques. It is fresh, original, and gathered with a specific purpose in mind.

#### Secondary Data
Secondary data is information collected by others for different purposes. It comes from sources such as government reports, research papers, historical databases, or industry publications.

![alt text](../../../assets/images/ml/data/2.jpeg)

[_Diagram from mermaid mind_](https://mermaid-mind.vercel.app/gallery/6799d5e08192d3f5b911fd01)

## Quality Assurance of Primary Data

The quality of primary data depends on how it is collected. To ensure high-quality data, it is essential to follow certain standards and governance protocols. Below are some key techniques to maintain data quality:

Here's a detailed description of techniques for ensuring primary data quality:

- **Defining Standard Variables**

The establishment of uniform variable names and formats across all data collection instruments ensures consistency and prevents confusion. For example, using standardized naming conventions like 'customer_id' instead of variations like 'cust_id' or 'customerID' makes data integration and analysis more reliable.

- **Units of Measurement**

Specifying and enforcing consistent units of measurement throughout the data collection process prevents conversion errors and misinterpretation. This includes clearly documenting whether measurements are in metric or imperial units, and maintaining the same unit system across all related data points.

- **Data Type Constraints**

Implementing strict data type validation ensures that each field contains appropriate information in the correct format. This involves setting up proper data types (integer, string, date, etc.) and field length restrictions to maintain data integrity and prevent invalid entries.

- **Predefined Validation Messages**

Creating clear, informative error messages that appear when data entry rules are violated helps users understand and correct mistakes immediately. These messages should guide users on proper data format and acceptable values, reducing the likelihood of incorrect data submission.

- **Dropdown Menus**

Incorporating dropdown lists for fields with predetermined options eliminates spelling errors and ensures data consistency. This approach also speeds up data entry and reduces the cognitive load on users by presenting them with valid choices rather than requiring manual input.

- **Acknowledgments**

Implementing confirmation steps or acknowledgment processes ensures that users verify critical data before submission. This creates an additional layer of quality control and makes users more accountable for the accuracy of their entries.

- **Metadata Language**

Developing comprehensive metadata documentation that describes data elements, their relationships, and their context ensures long-term data usability and understanding. This includes clear definitions, data dictionaries, and documentation of any changes or updates to the data structure.

- **Question Relevancy**

Ensuring that data collection questions are pertinent to the research objectives and are clearly understood by respondents improves response quality. This involves careful question design and testing to confirm that each item captures the intended information effectively.

![alt text](../../../assets/images/ml/data/3.jpg)

## Quality Assurance of Secondary Data

Since secondary data is collected from external sources, ensuring its quality requires additional steps:

1. **Source Credibility**
   - Verify the reputation of the data provider.
   - Cross-reference multiple sources for accuracy.

2. **Timeliness and Relevance**
   - Check publication dates to ensure data is up-to-date.
   - Evaluate whether the data aligns with the current research or business needs.

3. **Data Consistency**
   - Compare similar datasets to identify discrepancies.
   - Use statistical methods to detect anomalies.

4. **Data Transformation and Standardization**
   - Convert data into a uniform structure.
   - Apply normalization techniques to maintain consistency across datasets.

## Conclusion

Data quality assurance and governance play a fundamental role in any data-driven decision-making process. Whether dealing with primary or secondary data, following best practices in data collection, validation, and preprocessing ensures reliable insights and better model performance.

By implementing rigorous data quality measures, organizations can enhance the trustworthiness of their data and drive more effective, accurate, and impactful decision-making processes.

## References

1. [Everyone Wants to Do the Model Work, Not the Data Work](https://dl.acm.org/doi/abs/10.1145/3411764.3445518)
2. [Top 10 Data Quality Best Practices to Improve Data Performance - Atlan](https://atlan.com/data-quality-best-practices/)
