INSERT INTO libraryapp_library
(name, address)
VALUES
('Bellview Library', '500 Main Street');

INSERT INTO libraryapp_book
(title, isbn, author, year_published, publisher, librarian_id, location_id)
VALUES
('Lamb', '59359509', 'Christopher Moore', 2004, "some publishing co.", 1, 1);

INSERT INTO libraryapp_book
(title, isbn, author, year_published, publisher, librarian_id, location_id)
VALUES
('Taiko', '0472809124893', 'Eiji Yoshikawa', 2001,"some publishing co.", 1, 1);

INSERT INTO libraryapp_book
(title, isbn, author, year_published, publisher, librarian_id, location_id)
VALUES
('The Lion, the Witch and the Wardrobe', '04721239124893', 'C.S. Lewis', 1950,"Geoffrey Bles", (SELECT id FROM auth_user WHERE first_name="Ricky" ), 1);