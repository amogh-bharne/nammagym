DELIMITER //
CREATE TRIGGER after_insert_payment
AFTER INSERT ON Payments
FOR EACH ROW
BEGIN
    DECLARE membership_duration INT;

    SET membership_duration = 30;

    UPDATE Members
    SET MembershipExpiry = DATE_ADD(NEW.PaymentDate, INTERVAL membership_duration DAY)
    WHERE MemberID = NEW.MemberID;
END;
//
DELIMITER ;

