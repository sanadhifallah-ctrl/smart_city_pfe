from sqlalchemy.orm import Session
from app.models.route_report import RouteReport, StopStatus
from app.schemas.route_report import RouteReportCreate, RouteReportUpdate


def create_route_report(db: Session, data: RouteReportCreate):
    new_stop = RouteReport(
        route_id=data.route_id,
        report_id=data.report_id,
        visit_order=data.visit_order,
    )
    db.add(new_stop)
    db.commit()
    db.refresh(new_stop)
    return new_stop


def get_route_report_by_id(db: Session, route_report_id: int):
    return db.query(RouteReport).filter(RouteReport.id == route_report_id).first()


def get_stops_by_report(db: Session, report_id: int):
    return db.query(RouteReport).filter(RouteReport.report_id == report_id).all()


def update_route_report(db: Session, stop: RouteReport, data: RouteReportUpdate):
    if data.status is not None:
        stop.status = data.status
    if data.agent_notes is not None:
        stop.agent_notes = data.agent_notes
    if data.visited_at is not None:
        stop.visited_at = data.visited_at
    if data.visit_order is not None:
        stop.visit_order = data.visit_order
    db.commit()
    db.refresh(stop)
    return stop


def delete_route_report(db: Session, route_report_id: int):
    stop = get_route_report_by_id(db, route_report_id)
    if stop:
        db.delete(stop)
        db.commit()
    return stop