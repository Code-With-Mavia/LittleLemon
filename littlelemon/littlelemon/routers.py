# littlelemon/routers.py

class ReservationRouter:
    """
    Routes database operations for the Booking model to the 'reservations' database.
    All other models use the 'default' database.
    """

    def db_for_read(self, model, **hints):
        """Direct read operations for Booking to 'reservations'."""
        if model._meta.app_label == 'restaurant' and model.__name__ == 'Booking':
            return 'reservations'
        return 'default'

    def db_for_write(self, model, **hints):
        """Direct write operations for Booking to 'reservations'."""
        if model._meta.app_label == 'restaurant' and model.__name__ == 'Booking':
            return 'reservations'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both objects are in the same database
        or if either is the Booking model.
        """
        db_list = ('default', 'reservations')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the Booking model only appears in the 'reservations' database.
        All other models go to 'default'.
        """
        if app_label == 'restaurant' and model_name == 'booking':
            return db == 'reservations'
        elif app_label == 'restaurant':
            # Other restaurant models (like Menu) go to default
            return db == 'default'
        return None
