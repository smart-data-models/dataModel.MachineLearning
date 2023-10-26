/* (Beta) Export of data model MLProcessing of the subject dataModel.MachineLearning for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE MLProcessing_type AS ENUM ('MLProcessing');
CREATE TABLE MLProcessing (alternateName TEXT, connectionParameters JSON, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, dueDate TIMESTAMP, id TEXT PRIMARY KEY, name TEXT, objective TEXT, owner JSON, seeAlso JSON, source TEXT, type MLProcessing_type);