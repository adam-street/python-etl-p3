from google.cloud import bigquery
import pgsql
import sql
from pgsql import query
import json

if __name__ == '__main__':

    # pgsql.query(sql.create_schema)
    # pgsql.query(sql.create_table, [""])

    client = bigquery.Client()

    query = client.query(
        """
            SELECT geo_id, sub_region_1 AS state, sub_region_2 AS county, percent_change AS sales_vector
            FROM(
                SELECT geo_id, sub_region_1, sub_region_2, census_fips_code, AVG(retail_and_recreation_percent_change_from_baseline) AS percent_change
                FROM bigquery-public-data.census_bureau_acs.county_2017_1yr
                JOIN bigquery-public-data.covid19_google_mobility.mobility_report ON geo_id || '.0' = census_fips_code
                WHERE median_rent < 2000 AND median_age < 30
                GROUP BY geo_id, sub_region_1, sub_region_2, census_fips_code)
            WHERE percent_change  > -15 LIMIT 50;
        """
    )

    for i in query.result():
        result_list = []
        for item in i:
            result_list.append(item)
        pgsql.query(sql.create_insert, result_list)