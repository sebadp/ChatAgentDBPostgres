# ChatAgentDB Usage Guide

This guide will teach you how to make the most of ChatAgentDB to interact with your PostgreSQL database using natural language.

## 🚀 Getting Started

Once you have connected ChatAgentDB to your database (following the instructions in [setup.md](setup.md)), you'll be ready to start making queries.

### Main Interface

The ChatAgentDB interface consists of:

1. **Sidebar** - Database connection configuration
2. **Chat area** - Where you interact with the agent and see the results
3. **Schema summary** - Once connected, shows information about the available tables

## 💬 Asking Questions

You can ask questions in natural language about your data. The agent will:
- Translate your questions into SQL
- Execute the queries on your database
- Present the results in an understandable way

### Basic Question Examples

- "What tables are in the database?"
- "Show the first 5 records from the users table"
- "How many products do we have in total?"
- "What is the average price of products?"

### Intermediate Question Examples

- "What are the 3 best-selling products this month?"
- "Show total sales by region, ordered from highest to lowest"
- "Which customers have spent more than $1000 in the last quarter?"
- "Compare this month's sales with last month's"

### Advanced Question Examples

- "Calculate the customer retention rate month by month during the last year"
- "Show a cohort analysis of users who registered in January"
- "What is the correlation between product price and sales volume?"
- "Identify products with seasonal sales patterns based on historical data"

## 🧠 Effective Techniques

### Providing Context

To get better results, it's helpful to provide additional context:

❌ **Less effective**: "Show sales data"

✅ **More effective**: "Show total sales by product category for the first quarter of 2024"

### Specific Format Requests

You can request specific formats for the results:

- "Show the results ordered by date descending"
- "Present this data as percentages"
- "Calculate the percentage difference between these periods"

### Multiple Queries

You can chain complex analyses:

"First show the monthly sales from last year, then calculate the month-to-month growth rate, and finally identify the months with negative growth"

### Exploratory Queries

If you're not familiar with the schema:

1. "What tables are in this database?"
2. "Show the structure of the customers table"
3. "What fields does the orders table have?"

## 📊 Common Use Cases

### Sales Analysis

- "What was the total revenue for the last quarter broken down by product line?"
- "Show the weekly sales trend over the last 3 months"
- "Compare the sales performance of the east and west regions"

### User Analysis

- "What is the conversion rate from registered users to buyers?"
- "Show the distribution of users by age group and gender"
- "What percentage of users has been inactive for more than 30 days?"

### Inventory Management

- "Identify products with fewer than 10 units in stock"
- "What is the inventory turnover by product category?"
- "Show products that need restocking based on sales trends"

## 🔍 Query Debugging

If the results aren't what you expected:

1. **Be more specific**: "In the 'sales' table, show only completed transactions from April 2024"
2. **Rephrase the question**: "Alternatively, can you show me the total daily sales from last month?"
3. **Ask for an explanation**: "Can you explain how you arrived at this result?"
4. **Correct assumptions**: "No, the users table doesn't have an 'age' field, use 'birth_date' to calculate age"

## 🚫 Limitations

Keep these limitations in mind when using ChatAgentDB:

- **Write operations**: For security, the agent is primarily configured for read queries (SELECT)
- **Performance with large datasets**: Complex queries on very large databases may take time
- **Very specialized queries**: Some very domain-specific queries may require refinement
- **Tables without clear relationships**: The agent works best with well-structured schemas with explicit relationships

## 🔄 Maintaining Context

ChatAgentDB maintains the context of the conversation, allowing you to ask follow-up questions:

1. "Show sales from last month"
2. "What were the 3 best-selling products?"
3. "Which customers bought these products?"

## 📋 Complete Session Examples

### Example 1: Sales Performance Analysis

```
User: "How many total sales did we have in 2023?"
Agent: [Shows total sales for 2023]

User: "How does that compare to 2022?"
Agent: [Shows comparison between 2023 and 2022]

User: "Broken down by quarter, which was our best period?"
Agent: [Shows quarterly analysis]

User: "For the best quarter, show the breakdown by product"
Agent: [Shows products sold in that quarter]
```

### Example 2: User Investigation

```
User: "How many new users registered in March?"
Agent: [Shows count of new users]

User: "What regions do they primarily come from?"
Agent: [Shows geographic distribution]

User: "What percentage of them have made at least one purchase?"
Agent: [Shows conversion rate]
```

## 🛠️ Best Practices

1. **Start with simple queries** to familiarize yourself with your data
2. **Build gradually** toward more complex analyses
3. **Provide feedback** to help the agent refine its responses
4. **Verify results** for critical queries
5. **Use consistent terms** that match your database schema

## 📚 Additional Resources

To learn more about working with databases and data analysis:

- [Official PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SQL Guide for Data Analysis](https://mode.com/sql-tutorial/)
- [Data Modeling Best Practices](https://www.datacamp.com/community/tutorials/database-design-tutorial)