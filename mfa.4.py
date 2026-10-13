{% extends "base.html" %}
{% block content %}
<h2>Welcome, {{ username }}</h2>
<p>Both authentication steps were completed successfully.</p>

<form method="post">
    <button type="submit">Record Attendance</button>
</form>

<h3>Attendance History</h3>
{% if records %}
    <ul>
    {% for record in records %}
        <li>{{ record["checkin_time"] }}</li>
    {% endfor %}
    </ul>
{% else %}
    <p>No attendance records yet.</p>
{% endif %}

<a href="{{ url_for('logout') }}">Logout</a>
{% endblock %}
