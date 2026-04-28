from sqlalchemy.orm import Session
from app.models.report import Report
from app.schemas.report import CreatReport, ReportUpdate


def create_report(db: Session, data: CreatReport, citizen_id: int):
    new_report = Report(
        citizen_id=citizen_id,        
        latitude=data.latitude,
        longitude=data.longitude,
        address_text=data.address_text,
        audio_path=data.audio_path,
    )
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report


def get_report_by_id(db: Session, report_id: int):
    return db.query(Report).filter(Report.id == report_id).first()


def get_all_reports(db: Session):
    return db.query(Report).all()


def get_reports_by_citizen(db: Session, citizen_id: int):
    return db.query(Report).filter(Report.citizen_id == citizen_id).all()

   
def update_report(db: Session, report: Report, data: ReportUpdate):
    if data.status is not None:
        report.status = data.status
    if data.description is not None:
        report.description = data.description
    if data.waste_type is not None:
        report.waste_type = data.waste_type
    if data.priority is not None:
        report.priority = data.priority
    if data.is_verified is not None:
        report.is_verified = data.is_verified
    db.commit()
    db.refresh(report)
    return report

def delete_report(db: Session, report_id: int):
    report = get_report_by_id(db, report_id)
    if report:
        db.delete(report)
        db.commit()
    return report