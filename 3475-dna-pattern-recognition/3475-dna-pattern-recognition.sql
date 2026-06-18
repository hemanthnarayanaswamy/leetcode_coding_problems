# Write your MySQL query statement below
select sample_id, dna_sequence, species,
(case when dna_sequence LIKE 'ATG%' then 1 else 0 end) as has_start,
(case when RIGHT(dna_sequence, 3) IN ('TAA', 'TAG', 'TGA') then 1 else 0 end) as has_stop,
(case when dna_sequence LIKE '%ATAT%' then 1 else 0 end) as has_atat,
(case when dna_sequence LIKE '%GGG%' then 1 else 0 end) as has_ggg
from Samples
