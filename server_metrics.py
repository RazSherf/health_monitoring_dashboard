import psutil

def get_cpu_usage():
    """Returns the CPU usage as a percentage."""
    return psutil.cpu_percent(interval=1)

def get_process_info():
    """Returns a list of running processes with basic information."""
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'status'])]
    return processes

def format_bytes(size):
    """Convert bytes to a human-readable format (e.g., GB, MB)."""
    # 1024 bytes = 1 KB, 1024 KB = 1 MB, etc.
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
        
        
def get_memory_usage():
    """Returns memory usage statistics."""
    memory = psutil.virtual_memory()
    return {
        'total': memory.total,
        'used': memory.used,
        'available': memory.available,
        'percent': memory.percent
    }


def get_disk_usage():
    """Returns disk usage statistics in a readable format while keeping the percentage as a number."""
    disk = psutil.disk_usage('/')
    return {
        'total': format_bytes(disk.total),
        'used': format_bytes(disk.used),
        'free': format_bytes(disk.free),
        'percent': disk.percent  # Keep this as a float for comparison purposes
    }

def get_health_status():
    """Combines metrics to give an overall health status."""
    cpu_percent = get_cpu_usage()
    memory_stats = get_memory_usage()
    disk_stats = get_disk_usage()

    health_status = {
        'cpu_usage': cpu_percent,
        'memory_usage': memory_stats['percent'],
        'disk_usage': disk_stats['percent'],
        'status': 'healthy' if cpu_percent < 85 and memory_stats['percent'] < 85 and disk_stats['percent'] < 85 else 'unhealthy'
    }
    return health_status
