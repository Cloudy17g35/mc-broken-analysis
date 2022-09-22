import streamlit as st
from datetime import datetime
from src import report
import settings
from logger import Logger

logs:Logger = Logger('app.log')


if __name__ == '__main__':
    date_input:datetime.date  = st.date_input(
        label='Please, choose date',
        min_value=settings.min_date,
        max_value=settings.max_date
    )
    logs.info(f'selected date: {date_input}')
    try:
        lost_revenue:float = report.sum_daily_lost_revenue_for_date(date_input)
        if lost_revenue is not None:
            st.write(f'Lost Revenue: {lost_revenue}')
        else:
            logs.info(f'Data not found for this date: {date_input}')
            st.write(f"There's no data for this date: {date_input}")
    except Exception as E:
        logs.info(f'Error occured while calculating report for this date: {date_input}, Error: {E}')
        st.write(f'Error occured while calculating report for this date: {date_input}')
