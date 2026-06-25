# Write your MySQL query statement below
select a.book_id, a.title, a.author, a.genre, a.publication_year, count(b.record_id) as current_borrowers
from library_books a
inner join borrowing_records b on a.book_id = b.book_id
where b.return_date is null
group by a.book_id
having a.total_copies = count(b.record_id)
order by current_borrowers desc, a.title asc