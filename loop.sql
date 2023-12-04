DO $$ 
DECLARE
    i INT;
BEGIN
    -- Insert data into financials table
    FOR i IN 20..30 LOOP
        INSERT INTO financials (financials_id, total_gross, inflation_adjusted_gross)
        VALUES (i, i * 1000000, i * 900000);
    END LOOP;

    -- Insert data into rating table
    INSERT INTO rating (mpaa_rating, rating_id) VALUES ('G', 4);
    INSERT INTO rating (mpaa_rating, rating_id) VALUES ('PG', 5);
    INSERT INTO rating (mpaa_rating, rating_id) VALUES ('PG-13', 6);

    -- Insert data into movie table
    FOR i IN 1..10 LOOP
        INSERT INTO movie (movie_id, title, release_date, genre, financials_id, rating_id)
        VALUES (i, 'Movie' || i, CURRENT_DATE - (i * 30), 'Genre' || i, i, i % 5 + 1);
    END LOOP;
END $$;
