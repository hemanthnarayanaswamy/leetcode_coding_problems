# Write your MySQL query statement below
select lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year, t2.not_returned as current_borrowers
from library_books lb
join (
        select book_id, Count(*) as not_returned
        from borrowing_records 
        where ISNULL(return_date) 
        group by book_id
     ) t2 on t2.book_id = lb.book_id
where (lb.total_copies - t2.not_returned) = 0
order by current_borrowers DESC, lb.title ASC