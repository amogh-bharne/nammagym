DELIMITER //
CREATE PROCEDURE GetActiveMembersCount()
BEGIN
    SELECT COUNT(*) AS ActiveMembersCount
    FROM Members
    WHERE MembershipExpiry >= CURDATE();
END;
//
DELIMITER ;
