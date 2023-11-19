﻿USE [master]
GO
CREATE LOGIN [etl] WITH PASSWORD=N'', DEFAULT_DATABASE=[AdventureWorksDW2019], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
USE [AdventureWorksDW2019]
GO
CREATE USER [etl] FOR LOGIN [etl]
GO
USE [AdventureWorksDW2019]
GO
ALTER ROLE [db_datareader] ADD MEMBER [etl]
GO
use [master]
GO
GRANT CONNECT SQL TO [etl]
GO