CREATE TABLE "Kit"(
    "id" serial NOT NULL,
    "nome_instrumento" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Kit" ADD PRIMARY KEY("id");
CREATE TABLE "Cirurgia"(
    "id" serial NOT NULL,
    "CRM_Medico" INTEGER NOT NULL,
    "CPF_Paciente" INTEGER NOT NULL,
    "Sala_Hospital" INTEGER NOT NULL,
    "Kit_id" INTEGER NOT NULL,
    "Tipo_Cirurgia" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Cirurgia" ADD PRIMARY KEY("id");
ALTER TABLE
    "Cirurgia" ADD CONSTRAINT "cirurgia_kit_id_foreign" FOREIGN KEY("Kit_id") REFERENCES "Kit"("id");



