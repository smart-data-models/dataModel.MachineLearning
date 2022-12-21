/* (Beta) Export of data model MLProcessing of the subject dataModel.MachineLearning for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE MLProcessing_type AS ENUM ('MLProcessing');
CREATE TABLE MLProcessing (alternateName text, connectionParameters json, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, dueDate timestamp, id text, name text, objective text, owner json, refMLModel text, refSubscriptionQuery text, seeAlso json, source text, type MLProcessing_type);