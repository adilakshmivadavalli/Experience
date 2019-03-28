1CREATE TABLE [dbo].[Department](
	[DeptID] [int] IDENTITY(1,1) NOT NULL,
	[DeptName] [varchar](50) NOT NULL,


1CREATE TABLE [dbo].[Device](
	[DeviceID] [int] IDENTITY(1,1) NOT NULL,
	[DWID] [int] NOT NULL,
	[DeviceName] [varchar](50) NOT NULL,


1CREATE TABLE [dbo].[DeviceApply](
	[DeviceID] [int] NOT NULL,
	[DeptID] [int] NOT NULL,
	[ApplyDate] [date] NOT NULL,
	[QuantityApplied] [int] NOT NULL,


1CREATE TABLE [dbo].[Provider](
	[DPID] [int] IDENTITY(1,1) NOT NULL,
	[DPName] [varchar](50) NOT NULL,
	[DPAddress] [varchar](100) NOT NULL,
	[DPPhoneNumber] [varchar](20) NOT NULL,
	[DPEmail] [varchar](40) NULL,


1CREATE TABLE [dbo].[ProvideDetail](
	[DPID] [int] NOT NULL,
	[DeviceID] [int] NOT NULL,
	[DevicePrice] [money] NOT NULL,
	[DeviceQuantity] [int] NOT NULL,
	[PurchaseDate] [date] NOT NULL,


1CREATE TABLE [dbo].[DeviceReturn](
	[DeviceID] [int] NOT NULL,
	[DeptID] [int] NOT NULL,
	[ReturnDate] [date] NOT NULL,
	[QuantityReturned] [int] NOT NULL,	


1CREATE TABLE [dbo].[DeviceWarehouse](
	[DWID] [int] NOT NULL,
	[DeviceID] [int] NOT NULL,
	[DeviceQuantity] [int] NOT NULL,


CREATE TABLE [dbo].[Manager](
ManagerID
DeptID
SSN
LastName
FirstName
