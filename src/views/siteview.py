#/src/views/siteview.py
from flask import request, g, Blueprint, json, Response
from ..shared.authentication import Auth
from ..models.site import SiteModel, SiteSchema

site_api = Blueprint('sites', __name__)
site_schema = SiteSchema()


@site_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
    """
    Create Sites Function
    """
    req_data = request.get_json()
    try:
        data = site_schema.load(req_data)
    except:
        message = {"error": "Either required fields are missing or incorrect fields provided"}
        return custom_response(message, 400)
    site = SiteModel(data)
    site.save()
    data = site_schema.dump(site)
    return custom_response(data, 201)


@site_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
    """
    Get All Sites
    """
    sites = SiteModel.get_all_sites()
    data = site_schema.dump(sites, many=True)
    return custom_response(data, 200)


@site_api.route('/<int:site_id>', methods=['GET'])
@Auth.auth_required
def get_one(site_id):
    """
    Get A Site
    """
    site = SiteModel.get_one_site(site_id)
    if not site:
        return custom_response({'error': 'site not found'}, 404)
    data = site_schema.dump(site)
    return custom_response(data, 200)


@site_api.route('/<int:site_id>', methods=['PUT'])
@Auth.auth_required
def update(site_id):
    """
    Update me
    """
    req_data = request.get_json()
    site = SiteModel.get_one_site(site_id)
    if not site:
        message = {"error": "site not found"}
        return custom_response(message, 404)
    try:
        data = site_schema.load(req_data)
    except:
        message = {"error": "Either required fields are missing or incorrect fields provided"}
        return custom_response(message, 400)
    site.update(data)
    ser_site = site_schema.dump(site)
    return custom_response(ser_site, 200)


@site_api.route('/<int:site_id>', methods=['DELETE'])
@Auth.auth_required
def delete(site_id):
    """
    Delete a site
    """
    site = SiteModel.get_one_site(site_id)
    if not site:
        message = {"error": "site not found"}
        return custom_response(message, 404)
    site.delete()
    return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
        )