import pgsql
import sql
from google.cloud import bigquery;

if __name__ == '__main__':
    client = bigquery.Client()
    query = client.query(
        """
        SELECT geo_id, sub_region_1 AS state, sub_region_2 AS county, change AS sales_vector FROM (
        SELECT geo_id, sub_region_1, sub_region_2, census_fips_code, AVG(retail_and_recreation_percent_change_from_baseline) AS change FROM bigquery-public-data.census_bureau_acs.county_2017_1yr
        JOIN bigquery-public-data.covid19_google_mobility.mobility_report ON geo_id || '.0' = census_fips_code
        WHERE median_rent < 2000 AND median_age < 30
        GROUP BY geo_id, sub_region_1, sub_region_2, census_fips_code)
        WHERE change > -15;
        """
    )

    pgsql.pgquery(sql.create_schema, ["My Insert!"])

    for row in query.result():
        info = []
        info.append(row.geo_id)
        info.append(row.state)
        info.append(row.county)
        info.append(row.sales_vector)
        pgsql.pgquery(sql.insert_data, info)