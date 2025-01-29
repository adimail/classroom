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

1. **Standardized Data Collection Methods**
   - Use well-defined procedures and structured formats.
   - Ensure consistency in survey questions and experiment protocols.

2. **Validation and Verification**
   - Cross-check responses for accuracy.
   - Implement double-entry verification to minimize errors.

3. **Data Cleaning and Preprocessing**
   - Remove duplicate entries and inconsistencies.
   - Normalize data formats (e.g., date formats, categorical variables).

4. **Bias Mitigation**
   - Ensure a diverse sample population.
   - Address missing values using imputation techniques.

5. **Automated Data Quality Checks**
   - Implement real-time validation during data entry.
   - Use anomaly detection algorithms to identify outliers.

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

## Data Quality Best Practices

Ensuring high data quality is essential for reliable analytics and decision-making. Here are some best practices to maintain data quality:

1. **Data Governance Framework**
   - Establish formal policies for data management.
   - Ensure consistent data handling across the organization.

2. **Regular Data Audits**
   - Conduct periodic checks to identify inconsistencies and errors.
   - Recommended frequency: at least once a year.

3. **Validation Rules and Checks**
   - Implement automated validation to catch errors in real-time.
   - Ensure data accuracy and relevance.

4. **Data Standardization**
   - Maintain uniform data formats for easy analysis.
   - Reduces misunderstandings and misinterpretations.

5. **Data Cleaning and Maintenance**
   - Regularly detect and correct data errors.
   - Use tools for maintaining data hygiene.

6. **Continuous Monitoring and Reporting**
   - Implement real-time monitoring tools.
   - Ensure data remains accurate and relevant.

7. **Data Source Verification**
   - Verify the reliability of data sources.
   - Cross-reference multiple sources for accuracy.

8. **User Training and Awareness**
   - Educate team members on the importance of data quality.
   - Reduce human errors through training.

9. **Backup and Data Recovery**
   - Schedule regular automated backups.
   - Test recovery processes periodically.

10. **Access Controls and Permissions**
    - Limit data access to authorized personnel.
    - Regularly review and update permissions.

## What is Data Quality Assurance and Why is it Needed?

Data Quality Assurance (DQA) is the process of ensuring that data is accurate, complete, reliable, and relevant. It is needed to make informed decisions, maintain operational efficiency, and avoid costly errors.

## Primary Data

Primary data is collected directly by researchers or model developers through surveys, experiments, or other techniques. It is fresh, original, and gathered with a specific purpose in mind.

## Defining Standards

Defining standards involves setting clear guidelines and protocols for data collection, validation, and processing to ensure consistency and accuracy.

## Using Pre-designed Indicators

Pre-designed indicators are predefined metrics or benchmarks used to measure data quality and ensure that data meets the required standards.

## Tips for Ensuring Data Quality for ODK

ODK (Open Data Kit) is a suite of tools for data collection. Here are some tips for ensuring data quality using ODK:

### Using Constraints in ODK

Constraints are rules applied to data fields to ensure that the data entered meets specific criteria.

### Using Required Fields in ODK

Required fields are mandatory fields that must be filled out before the form can be submitted.

### Using Select Instead of Text in ODK

Using select fields instead of text fields can reduce errors by providing predefined options for data entry.

### Using Hints in ODK

Hints are additional information or instructions provided to the user to help them enter data correctly.

### Using Acknowledgements in ODK

Acknowledgements are messages displayed to the user to confirm that their data has been successfully submitted.

### Using Relevant in ODK

The relevant feature in ODK allows you to show or hide questions based on the answers to previous questions.

### Using Metadata in ODK

Metadata is additional information about the data, such as the date and time of data collection, the location, and the device used.

## Language of the Data Collection Tool

The language used in the data collection tool should be clear, concise, and easily understandable by the respondents.

## Paper Questionnaires

Paper questionnaires should be designed with clear instructions and easy-to-follow formats to ensure accurate data collection.

## Testing Data Collection Tools

Testing data collection tools involves conducting pilot tests to identify and fix any issues before the actual data collection begins.

## Training

Training is essential to ensure that data collectors understand the data collection process, the tools used, and the importance of data quality.

## Data Quality Checks

Data quality checks involve reviewing the collected data for accuracy, completeness, and consistency.

## Follow Up Interviews

Follow-up interviews are conducted to verify the accuracy of the collected data and to gather additional information if needed.

## Secondary Data

Secondary data is information collected by others for different purposes. It comes from sources such as government reports, research papers, historical databases, or industry publications.

## The Cost and Consequences of Poor Data Quality

Poor data quality can lead to significant financial losses and operational inefficiencies. Here are some examples:

1. **Retail Chain Overstock**
   - Incorrect sales data led to massive overstock and storage costs.

2. **Healthcare Billing Errors**
   - Data inaccuracies resulted in billing errors and legal actions.

3. **E-commerce Site Pricing Glitch**
   - Data input error caused significant financial losses and reputational damage.

## Conclusion

Data quality assurance and governance play a fundamental role in any data-driven decision-making process. Whether dealing with primary or secondary data, following best practices in data collection, validation, and preprocessing ensures reliable insights and better model performance.

By implementing rigorous data quality measures, organizations can enhance the trustworthiness of their data and drive more effective, accurate, and impactful decision-making processes.

## References

1. [Everyone Wants to Do the Model Work, Not the Data Work](https://dl.acm.org/doi/abs/10.1145/3411764.3445518)
2. [Top 10 Data Quality Best Practices to Improve Data Performance - Atlan](https://atlan.com/data-quality-best-practices/)
