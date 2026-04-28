from sqlalchemy.orm import Session
from app.models.route import route, RouteStatus
from app.schemas.route import RouteCreate, RouteUpdate


def create_route(db: Session, data: RouteCreate, admin_id: int):
    new_route = route(
        admin_id=admin_id,        
        agent_id=data.agent_id, 
    )
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route


def get_route_by_id(db: Session, route_id: int):
    return db.query(route).filter(route.id == route_id).first()


def get_all_routes(db: Session):
    return db.query(route).all()


def get_routes_by_agent(db: Session, agent_id: int):
    return db.query(route).filter(route.agent_id == agent_id).all()


def get_routes_by_status(db: Session, status: RouteStatus):
    return db.query(route).filter(route.status == status).all()


def update_route(db: Session, route: Route, data: RouteUpdate):
    if data.agent_id is not None:
        route.agent_id = data.agent_id
    if data.status is not None:
        route.status = data.status
    if data.notes is not None:
        route.notes = data.notes
    if data.started_at is not None:
        route.started_at = data.started_at
    if data.completed_at is not None:
        route.completed_at = data.completed_at
    db.commit()
    db.refresh(route)
    return route

def delete_route(db: Session, route_id: int):
    route = get_route_by_id(db, route_id)
    if route:
        db.delete(route)
        db.commit()
    return route