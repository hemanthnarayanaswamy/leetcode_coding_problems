DELETE FROM Person
WHERE id NOT IN (
    select id
    from (
        select MIN(id) as id
        from person
        group by email
    ) t
)
