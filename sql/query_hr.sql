create table if not exists Absenteeism(
    ID INT PRIMARY KEY,
    Reason_absence INT,
    Month_absence INT,
    Day_of_week INT,
    Seasons INT,
    Transportation_expense INT,
    Distance_from_Residence_to_Work INT,
    Service_time INT,
    Age INT,
    Work_load_AverageDay VARCHAR(255),
    Hit_target INT,
    Disciplinary_failure INT,
    Education INT,
    Son INT,
    Social_drinker INT,
    Social_smoker INT,
    Pet INT,
    Weight INT,
    Height INT,
    Body_mass_index INT,
    Absenteeism_hours INT
);

create table if not exists Compensation(
    ID INT PRIMARY KEY,
    comp_hr INT
);

create table if not exists Reasons(
    Number INT PRIMARY KEY,
    Reason VARCHAR(255)
);


select * from Absenteeism limit 10;

select * from `Compensation` limit 10;

select * from `Reasons` limit 10;


create or REPLACE view v_full_data as (
    select a.*, c.comp_hr, r.Reason from `Absenteeism` a
    left join `Compensation` c on a.ID = c.ID
    left join `Reasons` r on a.Reason_absence = r.Number
);

-- find the helthiest employees for the bonus
select * from v_full_data
where `Social_drinker`=0 and `Social_smoker`=0
and `Body_mass_index` < 25 and 
`Absenteeism_hours` < (select avg(`Absenteeism_hours`) from `Absenteeism`);

--- Compensation rate increese for non-smokers
-- Budget = 983,221
select count(*) as non_smokers from `Absenteeism`
where `Social_smoker` = 0;

-- non smokers employees = 686
-- How much will be the compensation increese per hour for non-smokers?
-- Hours per year per person = 8 * 5 * 52 = 2080
-- 686 * 2080 = 1426880
-- 983221 / 1426880 = $ 0.69 per hour
-- That means that the yearly compensation for non-smokers will be +$1414.4.


-- Optimize query
create or replace view v_full_data as (
    select  a.ID,
            r.`Reason`,
            a.`Body_mass_index`,
            a.`Month_absence`,
            CASE WHEN a.`Body_mass_index` < 18.5 THEN 'Underweight'
                 WHEN a.`Body_mass_index` BETWEEN 18.5 AND 24.9 THEN 'Normal'
                 WHEN a.`Body_mass_index` BETWEEN 25 AND 29.9 THEN 'Overweight'
                 WHEN a.`Body_mass_index` > 30 THEN 'Obese'
                 ELSE 'Unknown'
                 END as BMI_Names,
            case WHEN a.`Month_absence` IN (12, 1, 2) THEN 'Winter'
                 WHEN a.`Month_absence` IN (3, 4, 5) THEN 'Spring'
                 WHEN a.`Month_absence` IN (6, 7, 8) THEN 'Summer'
                 WHEN a.`Month_absence` IN (9, 10, 11) THEN 'Autumn'
                 ELSE 'Unknown'
                 END as Seasons_Names,
            a.`Seasons`,
            a.`Day_of_week`,
            a.`Transportation_expense`,
            a.`Education`,
            a.`Son`,
            a.`Social_drinker`,
            a.`Social_smoker`,
            a.`Pet`,
            a.`Disciplinary_failure`,
            a.`Age`,
            a.`Work_load_AverageDay`,
            a. `Absenteeism_hours`,
            c.`comp_hr`
            from `Absenteeism` a
    left join `Compensation` c on a.ID = c.ID
    left join `Reasons` r on a.Reason_absence = r.Number
);

select * from v_full_data limit 10;