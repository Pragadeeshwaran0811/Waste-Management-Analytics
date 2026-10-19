create database waste_management;
use waste_management;
create table waste_data (
city_district varchar(100),
waste_type varchar(50),
waste_generated_tons_per_day INT,
recycling_rate_percent DECIMAL(5,2),
population_density INT,
municipal_efficiency_score DECIMAL(4,2),
disposal_method VARCHAR(50),
waste_management_cost_per_ton DECIMAL(10,2),
awareness_campaigns_count INT,
landfill_name VARCHAR(100),
landfill_location VARCHAR(100),
landfill_capacity_tons INT,
year INT
);
select * from waste_data;
select count(*)from waste_data;
select sum(waste_generated_tons_per_day) from waste_data; 
select avg(waste_generated_tons_per_day) from waste_data; 
select min(waste_generated_tons_per_day) from waste_data; 
select max(waste_generated_tons_per_day) from waste_data; 
select waste_type ,sum(waste_generated_tons_per_day) as total_waste from waste_data group by  waste_type order by total_waste desc;
select waste_type,avg(recycling_rate_percent) as average_waste from waste_data group by waste_type order by average_waste;
select sum(waste_generated_tons_per_day)as total_waste,year from waste_data group by year order by total_waste ;
select avg(recycling_rate_percent)as average_waste,year from waste_data group by year order by average_waste ;
select disposal_method,count(*)as record_count from waste_data group by disposal_method;
select disposal_method,avg(recycling_rate_percent) as average_recyling_rate from waste_data group by disposal_method;
select disposal_method,sum(waste_generated_tons_per_day) as total_waste_disposal_method from waste_data group by disposal_method order by total_waste_disposal_method desc;
select city_district ,sum(waste_generated_tons_per_day) as total_waste_by_cities from waste_data group by city_district order by total_waste_by_cities desc limit 5;
select city_district ,avg(recycling_rate_percent) as average_recycling_by_cities from waste_data group by city_district order by average_recycling_by_cities desc limit 1;
select city_district ,avg(recycling_rate_percent) as average_recycling_by_cities from waste_data group by city_district order by average_recycling_by_cities asc limit 1;
select city_district,avg(municipal_efficiency_score)as average_efficiency_score_cities from waste_data group by city_district order by average_efficiency_score_cities desc;
select waste_type,avg(waste_management_cost_per_ton )as average_waste_cost from waste_data group by waste_type order by average_waste_cost desc;
select  waste_type,sum(waste_generated_tons_per_day)as total_waste_generated ,avg(recycling_rate_percent) from waste_data group by waste_type; 
select waste_type,max(waste_management_cost_per_ton)as maximum_management_cost from waste_data group by waste_type;
select city_district,sum(waste_generated_tons_per_day)as total_waste_generated_city from waste_data group by city_district order by total_waste_generated_city asc limit 1;
select avg(recycling_rate_percent) as average_recyling_rate, awareness_campaigns_count from waste_data group by awareness_campaigns_count;
select avg(recycling_rate_percent) as average_recyling_rate,municipal_efficiency_score from waste_data group by municipal_efficiency_score;
select waste_type,sum(waste_generated_tons_per_day) as total_waste_generated from waste_data group by waste_type having total_waste_generated>900000;
select city_district,sum(waste_generated_tons_per_day) as total_waste_generated from waste_data group by city_district having total_waste_generated > 140000;
select city_district,avg(recycling_rate_percent),sum(waste_generated_tons_per_day) as total_waste_generated from waste_data group by city_district order by total_waste_generated desc limit 5;

