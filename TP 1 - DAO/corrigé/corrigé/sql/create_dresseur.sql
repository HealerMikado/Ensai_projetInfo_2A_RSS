create table dresseur (
    id  serial,
    name  varchar(40),
    PRIMARY KEY(id)
);

create table equipier(
    dresseurId integer REFERENCES dresseur(id),
    pokemonId integer REFERENCES pokedex(id),
    force integer default 0,
    PRIMARY KEY(dresseurId, pokemonId)
);