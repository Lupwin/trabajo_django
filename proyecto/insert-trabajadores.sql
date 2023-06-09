-- insert de Oficios
INSERT INTO public.servisarg_oficio(
	 nombre)
	VALUES
	('Carpinteria'),
	('Cerrajero'),
	('Albañil')
-- insert de trabajadores	
INSERT INTO public.servisarg_trabajador(
    id, nombre, apellido, fecha_nacimiento, dni, direccion, telefono, email, clave, descripcion, oficio_id
)
VALUES 
    (1, 'John', 'Doe', '1990-01-01', 12345678, '123 Main St', '5551234', 'john.doe@example.com', 'secreto', 'Lorem ipsum dolor sit amet', 1),
    (2, 'Jane', 'Smith', '1992-05-15', 87654321, '456 Oak St', '5559876', 'jane.smith@example.com', 'password', 'Lorem ipsum dolor sit amet', 2),
    (3, 'Mike', 'Johnson', '1985-09-30', 54321678, '789 Elm St', '5554567', 'mike.johnson@example.com', 'secret123', 'Lorem ipsum dolor sit amet', 3),
    (4, 'Emily', 'Brown', '1993-07-20', 98765432, '567 Maple Ave', '5557890', 'emily.brown@example.com', 'qwerty', 'Lorem ipsum dolor sit amet', 1),
    (5, 'David', 'Davis', '1988-03-12', 23456789, '890 Pine St', '5552345', 'david.davis@example.com', 'password123', 'Lorem ipsum dolor sit amet', 2),
    (6, 'Emma', 'Wilson', '1991-11-25', 76543210, '678 Oak Ave', '5556789', 'emma.wilson@example.com', 'abc123', 'Lorem ipsum dolor sit amet', 3),
    (7, 'Michael', 'Anderson', '1987-02-17', 34567890, '901 Elm St', '5553856', 'michael.anderson@example.com', 'pass123', 'Lorem ipsum dolor sit amet', 1),
    (8, 'Olivia', 'Miller', '1994-09-05', 10987654, '789 Maple Ave', '5553901', 'olivia.miller@example.com', 'qwerty123', 'Lorem ipsum dolor sit amet', 2),
    (9, 'James', 'Taylor', '1989-06-08', 45678901, '234 Pine St', '5545678', 'james.taylor@example.com', 'abc123456', 'Lorem ipsum dolor sit amet', 3),
    (10, 'Sophia', 'Moore', '1992-12-30', 21098765, '567 Oak Ave', '5539012', 'sophia.moore@example.com', 'pass123456', 'Lorem ipsum dolor sit amet', 1),
    (11, 'William', 'Anderson', '1986-04-13', 56789012, '901 Elm St', '5656759', 'william.anderson@example.com', 'qwertyabc', 'Lorem ipsum dolor sit amet', 2),
    (12, 'Ava', 'Thompson', '1993-01-08', 43210987, '789 Maple Ave', '5253456', 'ava.thompson@example.com', 'abcqwerty', 'Lorem ipsum dolor sit amet', 3),
    (13, 'Benjamin', 'Walker', '1988-08-21', 78901234, '234 Pine St', '5558901', 'benjamin.walker@example.com', 'passabc123', 'Lorem ipsum dolor sit amet', 1),
    (14, 'Mia', 'Harris', '1991-02-14', 54321098, '567 Oak Ave', '5555878', 'mia.harris@example.com', 'qwertypass', 'Lorem ipsum dolor sit amet', 2),
    (15, 'Alexander', 'Scott', '1987-10-27', 89012345, '901 Elm St', '5559012', 'alexander.scott@example.com', 'abcpass123', 'Lorem ipsum dolor sit amet', 3),
    (16, 'Ella', 'Martin', '1994-07-09', 21098165, '789 Maple Ave', '5556782', 'ella.martin@example.com', 'passqwerty123', 'Lorem ipsum dolor sit amet', 1),
    (17, 'Henry', 'Robinson', '1989-03-22', 65432109, '234 Pine St', '5553456', 'henry.robinson@example.com', 'abc123pass', 'Lorem ipsum dolor sit amet', 2),
    (18, 'Scarlett', 'Lewis', '1992-11-04', 43210997, '567 Oak Ave', '5558991', 'scarlett.lewis@example.com', 'passqwertyabc', 'Lorem ipsum dolor sit amet', 3),
    (19, 'Jacob', 'Young', '1986-06-17', 78901204, '901 Elm St', '5555608', 'jacob.young@example.com', 'abcqwerty123', 'Lorem ipsum dolor sit amet', 1),
    (20, 'Chloe', 'Walker', '1993-03-01', 54321008, '789 Maple Ave', '5059012', 'chloe.walker@example.com', 'pass123abcqwerty', 'Lorem ipsum dolor sit amet', 2);
