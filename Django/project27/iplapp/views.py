from django.shortcuts import render
from iplapp.models import CSKTable
from iplapp.models import DCTable
from iplapp.models import GTTable
from iplapp.models import KKRTable
from iplapp.models import LSGTable
from iplapp.models import MITable
from iplapp.models import PKTable
from iplapp.models import RCBTable
from iplapp.models import RRTable
from iplapp.models import SRHTable


from iplapp.forms import CSKTableForm
from iplapp.forms import DCTableForm
from iplapp.forms import GTTableForm
from iplapp.forms import KKRTableForm
from iplapp.forms import LSGTableForm
from iplapp.forms import MITableForm
from iplapp.forms import PKTableForm
from iplapp.forms import RCBTableForm
from iplapp.forms import RRTableForm
from iplapp.forms import SRHTableForm

# Create your views here.

def home_page(request):
	return render(request = request, template_name = 'iplapp/homepage.html')

def add_team(request):
	return render(request = request, template_name = 'iplapp/add.html')

def display_teamlist(request):
	return render(request = request, template_name = 'iplapp/display_teamlist.html')


def team_csk(request):
	csk_form = CSKTableForm()
	csk_dict = {'csk_form':csk_form}

	if request.method == 'POST':
		csk_form = CSKTableForm(request.POST)
		if csk_form.is_valid():
			csk_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/csk.html', context = csk_dict)


def team_dc(request):
	dc_form = DCTableForm()
	dc_dict = {'dc_form':dc_form}

	if request.method == 'POST':
		dc_form = DCTableForm(request.POST)
		if dc_form.is_valid():
			dc_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/dc.html', context = dc_dict)


def team_gt(request):
	gt_form = GTTableForm()
	gt_dict = {'gt_form':gt_form}

	if request.method == 'POST':
		gt_form = GTTableForm(request.POST)
		if gt_form.is_valid():
			gt_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/gt.html', context = gt_dict)


def team_kkr(request):
	kkr_form = KKRTableForm()
	kkr_dict = {'kkr_form':kkr_form}

	if request.method == 'POST':
		kkr_form = KKRTableForm(request.POST)
		if kkr_form.is_valid():
			kkr_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/kkr.html', context = kkr_dict)


def team_lsg(request):
	lsg_form = LSGTableForm()
	lsg_dict = {'lsg_form':lsg_form}

	if request.method == 'POST':
		lsg_form = LSGTableForm(request.POST)
		if lsg_form.is_valid():
			lsg_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/lsg.html', context = lsg_dict)


def team_mi(request):
	mi_form = MITableForm()
	mi_dict = {'mi_form':mi_form}

	if request.method == 'POST':
		mi_form = MITableForm(request.POST)
		if mi_form.is_valid():
			mi_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/mi.html', context = mi_dict)


def team_pk(request):
	pk_form = PKTableForm()
	pk_dict = {'pk_form':pk_form}

	if request.method == 'POST':
		pk_form = PKTableForm(request.POST)
		if pk_form.is_valid():
			pk_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/pk.html', context = pk_dict)


def team_rcb(request):
	rcb_form = RCBTableForm()
	rcb_dict = {'rcb_form':rcb_form}

	if request.method == 'POST':
		rcb_form = RCBTableForm(request.POST)
		if rcb_form.is_valid():
			rcb_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/rcb.html', context = rcb_dict)


def team_rr(request):
	rr_form = RRTableForm()
	rr_dict = {'rr_form':rr_form}

	if request.method == 'POST':
		rr_form = RRTableForm(request.POST)
		if rr_form.is_valid():
			rr_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/rr.html', context = rr_dict)


def team_srh(request):
	srh_form = SRHTableForm()
	srh_dict = {'srh_form':srh_form}

	if request.method == 'POST':
		srh_form = SRHTableForm(request.POST)
		if srh_form.is_valid():
			srh_form.save(commit = True)

	return render(request = request, template_name = 'iplapp/srh.html', context = srh_dict)


def list_team(request):
	csk_data = CSKTable.objects.all()
	dc_data = DCTable.objects.all()
	gt_data = GTTable.objects.all()
	kkr_data = KKRTable.objects.all()
	lsg_data = LSGTable.objects.all()
	mi_data = MITable.objects.all()
	pk_data = PKTable.objects.all()
	rcb_data = RCBTable.objects.all()
	rr_data = RRTable.objects.all()
	srh_data = SRHTable.objects.all()

	data_dict = {'csk_data':csk_data,'dc_data': dc_data,'gt_data':gt_data ,'kkr_data': kkr_data,'lsg_data':lsg_data ,'mi_data': mi_data,'pk_data': pk_data,'rcb_data':rcb_data ,'rr_data':rr_data ,'srh_data':srh_data ,}
	return render(request = request, template_name = 'iplapp/list.html', context = data_dict)


