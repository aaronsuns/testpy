+-----------------+          +-----------------+
|     Users       |          |      Roles      |
+-----------------+          +-----------------+
| UserID (PK)     |          | RoleName (PK)   |
| Role            | <----+   | Permissions     |
| Permissions     |      |   +-----------------+
+-----------------+      |
|
|
+-----------------+      |
|   Permissions   |      |
|    (List)       |      |
+-----------------+      |
|
v
+-----------------+
| RoleName        |
+-----------------+
| Permissions     |
+-----------------+



Table Name: Users

Attribute Name	Type	Description
UserID	String	Primary Key: Unique identifier for each user.
Role	String	Role assigned to the user (e.g., "admin", "user").
Permissions	List	(Optional) Directly assigned permissions, if any.


{
"UserID": "user123",
"Role": "admin",
"Permissions": ["read:data", "write:data"]
}



Table Name: Roles

Attribute Name	Type	Description
RoleName	String	Primary Key: Unique name of the role (e.g., "admin").
Permissions	List	List of permissions associated with this role.


{
"RoleName": "admin",
"Permissions": ["read:data", "write:data", "delete:data"]
}



