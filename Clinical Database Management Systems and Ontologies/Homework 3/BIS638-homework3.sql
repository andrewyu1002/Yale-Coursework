-- 1.
select distinct TestName 
from [dbo].[FlowCytometry] 
order by TestName;
----

-- 2.
select TestName, count(*) as Total
from [dbo].[FlowCytometry] 
group by TestName
order by Total desc;
----

-- 3.
select *
from (
    select 
        PatientName,
        SpecimenDt,
        CompleteDt,
        TestName,
        row_number() over (partition by TestName order by CompleteDt desc) as RowId
    from [dbo].[FlowCytometry]
) as ranked
where RowId <= 3
order by TestName, RowId;
----

-- 4.
select distinct
    PerformingLab,
    round(avg(cast(datediff(minute, SpecimenDt, CompleteDt) as float)/1440.0) 
          over (partition by PerformingLab), 2) as AvgTAT,
    round(percentile_cont(0.5) 
          within group (order by cast(datediff(minute, SpecimenDt, CompleteDt) as float)/1440.0) 
          over (partition by PerformingLab), 2) as MedianTAT
from [dbo].[FlowCytometry]
order by PerformingLab;
----

-- 5.
select SpecimenDayOfWeek, count(*) as Total
from [dbo].[FlowCytometry]
where PerformingLab = 'InsideLab'
group by SpecimenDayOfWeek
order by Total desc;
----

-- 6.
select 
    case SpecimenDayOfWeek
        when 'Monday' then 1
        when 'Tuesday' then 2
        when 'Wednesday' then 3
        when 'Thursday' then 4
        when 'Friday' then 5
        when 'Saturday' then 6
        when 'Sunday' then 7
    end as DayId,
    SpecimenDayOfWeek, 
	PerformingLab, 
	count(*) as Total
from [dbo].[FlowCytometry]
group by SpecimenDayOfWeek, PerformingLab
order by DayId, PerformingLab desc;
----