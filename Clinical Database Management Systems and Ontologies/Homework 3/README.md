# Description:
This project analyzes historical lab-ordering data for flow cytometry testing at a hospital that uses both an in-network and an out-of-network laboratory. The goal was to give hospital clinicians and administrators data-driven insight into test volume, patient-level detail, turnaround time, and day-of-week ordering patterns

# Skills Demonstrated:
- Tests Performed: Catalog every version of the flow cytometry test present in the data.
- Test Counts: Rank test versions by volume, most-ordered first.
- Find Examples: Surface the three most recently completed cases per test version for clinical chart review.
- Turnaround Time: Compare mean and median turnaround time (specimen collection → result completion) between the in-network and out-of-network labs.
- Day of Week (In-Network): Audit whether the in-network lab, which is not supposed to run tests on Fridays, has any exceptions.
- Day of Week (Out-of-Network): Extend the day-of-week audit to both labs to check whether the out-of-network lab is picking up unnecessary volume during the week.