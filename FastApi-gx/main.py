from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from fastapi.responses import HTMLResponse
import great_expectations as ge
import pandas as pd
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

# Get the DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

@app.get("/validate", response_class=HTMLResponse)
def validate_sales_data():
    # query to fetch data from the database
    query = "SELECT * FROM [great-expectations].dbo.Sales"
    with engine.connect() as connection:
        df = pd.read_sql_query(text(query), connection)

    # Ensure Order_ID column is treated as string
    df['Order_ID'] = df['Order_ID'].astype(str)

    # Initialize a Great Expectations DataFrame
    df_ge = ge.from_pandas(df)

    # Define expectations
    df_ge.expect_column_values_to_be_between("Total_Revenue", min_value=0)
    df_ge.expect_column_values_to_not_be_null("Total_Cost")
    df_ge.expect_column_values_to_be_between("Unit_Price", min_value=0, max_value=10000)
    df_ge.expect_column_values_to_not_be_null("Units_Sold")
    df_ge.expect_column_value_lengths_to_equal("Order_ID", 9)
    df_ge.expect_column_values_to_be_in_set("Order_Priority", ["H", "L", "C", "M"])
    df_ge.expect_column_values_to_be_in_set("Sales_Channel", ["offline", "online"])
    df_ge.expect_column_values_to_be_of_type("Country", "str")
    df_ge.expect_column_values_to_be_of_type("Region", "str")

    # Validate the data
    results = df_ge.validate()

    # Extract relevant results into a DataFrame
    results_summary = []
    for result in results["results"]:
        summary = {
            "Expectation": result["expectation_config"]["expectation_type"],
            "Column": result["expectation_config"]["kwargs"].get("column", ""),
            "Success": result["success"],
            "Details": result["result"],
        }
        results_summary.append(summary)

    results_df = pd.DataFrame(results_summary)

    # Format the DataFrame as an HTML table
    results_html = results_df.to_html(index=False)

    # Return the HTML table
    return HTMLResponse(content=results_html)

# Run the app with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
