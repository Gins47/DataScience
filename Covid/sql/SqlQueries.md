select \* from covid_dataset;

select location, date, total_cases, new_cases, total_deaths, population from covid_dataset order by 1,2;

-- Looking at total cases vs total deaths
-- Shows the likelyhood of dieing in Portugal
select location, date, total_cases, total_deaths, (total_deaths/total_cases)\*100 as DeathPercentage
from covid_dataset where location like '%Portugal%' order by 1,2;

--- Total Cases Vs Population
-- Percentage of population got covid
select location, date, total_cases, population, (total_cases/population)\*100 as totalCasePercent
from covid_dataset where location like '%Portugal%' order by 1,2;

-- Contries with highest infection vs population
select location, MAX(total_cases) as HigestInfection, population, MAX((total_cases/population))\*100 as PercentPopulationInfected
from covid_dataset Group by location, population order by PercentPopulationInfected desc;

-- Countires with highest death count per population
select location, MAX(cast(total_deaths as int)) as HigestDeath, population, MAX((total_deaths/population))\*100 as PercentPopulationDied
from covid_dataset where continent is not null and total_deaths is not null Group by location, population order by PercentPopulationDied desc;

-- Counties with Max death
select location, MAX(cast(total_deaths as int)) as HigestDeath,
from covid_dataset where continent is not null and total_deaths is not null Group by location, population order by HigestDeath desc;

-- Continent with maximum death

select location, MAX(cast(total_deaths as int)) as HighestDeath From covid_dataset
where continent is null
Group by location
order by HighestDeath desc;

--- Total cases , total death and percentage by date

select date,sum(new_cases) as Total_New_cases , sum(cast(new_deaths as int )) as Total_New_Deaths ,
sum(cast(new_deaths as int )) / sum(new_cases) \* 100 as New_Death_Percentage from covid_dataset
where continent is not null group by date order by 1,2;
